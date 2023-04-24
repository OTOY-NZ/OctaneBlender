import bpy
import bmesh
import math
import mathutils

# Calculate points on the Nurbs
# https://blender.stackexchange.com/questions/34145/calculate-points-on-a-nurbs-curve-without-converting-to-mesh

def macro_knotsu(nu):
    return nu.order_u + nu.point_count_u + (nu.order_u - 1 if nu.use_cyclic_u else 0)

def macro_segmentsu(nu):
    return nu.point_count_u if nu.use_cyclic_u else nu.point_count_u - 1

def makeknots(nu):
    knots = [0.0] * (4 + macro_knotsu(nu))
    flag = nu.use_endpoint_u + (nu.use_bezier_u << 1)
    if nu.use_cyclic_u:
        calcknots(knots, nu.point_count_u, nu.order_u, 0)
        makecyclicknots(knots, nu.point_count_u, nu.order_u)
    else:
        calcknots(knots, nu.point_count_u, nu.order_u, flag)
    return knots

def calcknots(knots, pnts, order, flag):
    pnts_order = pnts + order
    if flag == 1:
        k = 0.0
        for a in range(1, pnts_order + 1):
            knots[a - 1] = k
            if a >= order and a <= pnts:
                k += 1.0
    elif flag == 2:
        if order == 4:
            k = 0.34
            for a in range(pnts_order):
                knots[a] = math.floor(k)
                k += (1.0 / 3.0)
        elif order == 3:
            k = 0.6
            for a in range(pnts_order):
                if a >= order and a <= pnts:
                    k += 0.5
                    knots[a] = math.floor(k)
    else:
        for a in range(pnts_order):
            knots[a] = a

def makecyclicknots(knots, pnts, order):
    order2 = order - 1

    if order > 2:
        b = pnts + order2
        for a in range(1, order2):
            if knots[b] != knots[b - a]:
                break

            if a == order2:
                knots[pnts + order - 2] += 1.0

    b = order
    c = pnts + order + order2
    for a in range(pnts + order2, c):
        knots[a] = knots[a - 1] + (knots[b] - knots[b - 1])
        b -= 1

def basisNurb(t, order, pnts, knots, basis, start, end):
    i1 = i2 = 0
    orderpluspnts = order + pnts
    opp2 = orderpluspnts - 1

    # this is for float inaccuracy
    if t < knots[0]:
        t = knots[0]
    elif t > knots[opp2]:
        t = knots[opp2]

    # this part is order '1'
    o2 = order + 1
    for i in range(opp2):
        if knots[i] != knots[i + 1] and t >= knots[i] and t <= knots[i + 1]:
            basis[i] = 1.0
            i1 = i - o2
            if i1 < 0:
                i1 = 0
            i2 = i
            i += 1
            while i < opp2:
                basis[i] = 0.0
                i += 1
            break

        else:
            basis[i] = 0.0

    basis[i] = 0.0

    # this is order 2, 3, ...
    for j in range(2, order + 1):

        if i2 + j >= orderpluspnts:
            i2 = opp2 - j

        for i in range(i1, i2 + 1):
            if basis[i] != 0.0:
                d = ((t - knots[i]) * basis[i]) / (knots[i + j - 1] - knots[i])
            else:
                d = 0.0

            if basis[i + 1] != 0.0:
                e = ((knots[i + j] - t) * basis[i + 1]) / (knots[i + j] - knots[i + 1])
            else:
                e = 0.0

            basis[i] = d + e

    start = 1000
    end = 0

    for i in range(i1, i2 + 1):
        if basis[i] > 0.0:
            end = i
            if start == 1000:
                start = i

    return start, end

def nurb_make_curve(nu, resolu, stride):
    EPS = 1e-6
    coord_index = istart = iend = 0

    coord_array = [0.0] * (3 * nu.resolution_u * macro_segmentsu(nu))
    sum_array = [0] * nu.point_count_u
    basisu = [0.0] * macro_knotsu(nu)
    knots = makeknots(nu)

    resolu = resolu * macro_segmentsu(nu)
    ustart = knots[nu.order_u - 1]
    uend   = knots[nu.point_count_u + nu.order_u - 1] if nu.use_cyclic_u else \
             knots[nu.point_count_u]
    ustep  = (uend - ustart) / (resolu - (0 if nu.use_cyclic_u else 1))
    cycl = nu.order_u - 1 if nu.use_cyclic_u else 0

    u = ustart
    while resolu:
        resolu -= 1
        istart, iend = basisNurb(u, nu.order_u, nu.point_count_u + cycl, knots, basisu, istart, iend)

        #/* calc sum */
        sumdiv = 0.0
        sum_index = 0
        pt_index = istart - 1
        for i in range(istart, iend + 1):
            if i >= nu.point_count_u:
                pt_index = i - nu.point_count_u
            else:
                pt_index += 1

            sum_array[sum_index] = basisu[i] * nu.points[pt_index].co[3]
            sumdiv += sum_array[sum_index]
            sum_index += 1

        if (sumdiv != 0.0) and (sumdiv < 1.0 - EPS or sumdiv > 1.0 + EPS):
            sum_index = 0
            for i in range(istart, iend + 1):
                sum_array[sum_index] /= sumdiv
                sum_index += 1

        coord_array[coord_index: coord_index + 3] = (0.0, 0.0, 0.0)

        sum_index = 0
        pt_index = istart - 1
        for i in range(istart, iend + 1):
            if i >= nu.point_count_u:
                pt_index = i - nu.point_count_u
            else:
                pt_index += 1

            if sum_array[sum_index] != 0.0:
                for j in range(3):
                    coord_array[coord_index + j] += sum_array[sum_index] * nu.points[pt_index].co[j]
            sum_index += 1

        coord_index += stride
        u += ustep

    return coord_array

def calculate_points_on_nurbs_spline(spline, resolution):
    points_array = nurb_make_curve(spline, resolution, 3)
    return points_array

def calculate_points_on_bezier_segment(knot1, handle1, handle2, knot2, resolution):
    points_array = []
    vertices_array = mathutils.geometry.interpolate_bezier(knot1, handle1, handle2, knot2, resolution)
    for vertex_idx in range(len(vertices_array)):
        idx = vertex_idx * 3
        points_array.append(vertices_array[vertex_idx][0])
        points_array.append(vertices_array[vertex_idx][1])
        points_array.append(vertices_array[vertex_idx][2])
    return points_array

def calculate_points_on_bezier_spline(spline, resolution):
    points_array = []
    bzp = spline.bezier_points
    for i in range(len(bzp)):
        if i + 1 >= len(bzp):
            continue
        segment_points_array = calculate_points_on_bezier_segment(bzp[i].co, bzp[i].handle_right, bzp[i + 1].handle_left, bzp[i + 1].co, resolution + 1)
        if len(points_array) == 0:
            points_array.extend(segment_points_array)
        else:
            points_array.extend(segment_points_array[3:])
    if spline.use_cyclic_u:
        segment_points_array = calculate_points_on_bezier_segment(bzp[-1].co, bzp[-1].handle_right, bzp[0].handle_left, bzp[0].co, resolution + 1)
        if len(points_array) == 0:
            points_array.extend(segment_points_array)
        else:
            points_array.extend(segment_points_array[3:])
    return points_array

def calculate_points_on_curve(curve, is_viewport):
    curve_points_data = []
    for spline in curve.splines:
        spline_points_data = []
        resolution = (curve.render_resolution_u if curve.render_resolution_u else curve.resolution_u)
        if spline.type == "BEZIER":
            spline_points_data = calculate_points_on_bezier_spline(spline, resolution)
        elif spline.type == "NURBS":
            spline_points_data = calculate_points_on_nurbs_spline(spline, resolution)
        curve_points_data.append(spline_points_data)
    return curve_points_data