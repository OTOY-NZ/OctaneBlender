/*
 * Copyright 2011, Blender Foundation.
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 */

#ifndef __UTIL_TYPES_H__
#define __UTIL_TYPES_H__

#include <stdlib.h>

#define __device static inline

#if defined(_WIN32) && !defined(FREE_WINDOWS)
#   define __device_inline static __forceinline
#   define __align(...) __declspec(align(__VA_ARGS__))
#else
#   define __device_inline static inline __attribute__((always_inline))
#   define __forceinline inline __attribute__((always_inline))
#   define __align(...) __attribute__((aligned(__VA_ARGS__)))
#endif // #if defined(_WIN32) && !defined(FREE_WINDOWS)

/* Bitness */

#if defined(__ppc64__) || defined(__PPC64__) || defined(__x86_64__) || defined(__ia64__) || defined(_M_X64)
#   define __KERNEL_64_BIT__
#endif

#ifndef _WIN32
#include <stdint.h>
#endif

OCT_NAMESPACE_BEGIN

/* Types
 *
 * Define simpler unsigned type names, and integer with defined number of bits.
 * Also vector types, named to be compatible with OpenCL builtin types, while
 * working for CUDA and C++ too. */

/* Shorter Unsigned Names */

typedef unsigned char uchar;
typedef unsigned int uint;

/* Fixed Bits Types */

#ifdef _WIN32

typedef signed char int8_t;
typedef unsigned char uint8_t;

typedef signed short int16_t;
typedef unsigned short uint16_t;

typedef signed int int32_t;
typedef unsigned int uint32_t;

typedef long long int64_t;
typedef unsigned long long uint64_t;

#endif

/* Vector Types */

struct uchar2 {
	uchar x, y;

	__forceinline uchar operator[](int i) const { return *(&x + i); }
	__forceinline uchar& operator[](int i) { return *(&x + i); }
};

struct uchar3 {
	uchar x, y, z;

	__forceinline uchar operator[](int i) const { return *(&x + i); }
	__forceinline uchar& operator[](int i) { return *(&x + i); }
};

struct uchar4 {
	uchar x, y, z, w;

	__forceinline uchar operator[](int i) const { return *(&x + i); }
	__forceinline uchar& operator[](int i) { return *(&x + i); }
};

struct int2 {
	int x, y;

	__forceinline int operator[](int i) const { return *(&x + i); }
	__forceinline int& operator[](int i) { return *(&x + i); }
};

struct int3 {
	int x, y, z, w;

	__forceinline int operator[](int i) const { return *(&x + i); }
	__forceinline int& operator[](int i) { return *(&x + i); }
};

struct int4 {
	int x, y, z, w;

	__forceinline int operator[](int i) const { return *(&x + i); }
	__forceinline int& operator[](int i) { return *(&x + i); }
};

struct uint2 {
	uint x, y;

	__forceinline uint operator[](uint i) const { return *(&x + i); }
	__forceinline uint& operator[](uint i) { return *(&x + i); }
};

struct uint3 {
	uint x, y, z;

	__forceinline uint operator[](uint i) const { return *(&x + i); }
	__forceinline uint& operator[](uint i) { return *(&x + i); }
};

struct uint4 {
	uint x, y, z, w;

	__forceinline uint operator[](uint i) const { return *(&x + i); }
	__forceinline uint& operator[](uint i) { return *(&x + i); }
};

struct float2 {
	float x, y;

	__forceinline float operator[](int i) const { return *(&x + i); }
	__forceinline float& operator[](int i) { return *(&x + i); }
};
struct float3 {
	float x, y, z;

	__forceinline float operator[](int i) const { return *(&x + i); }
	__forceinline float& operator[](int i) { return *(&x + i); }
};

struct float4 {
	float x, y, z, w;

	__forceinline float operator[](int i) const { return *(&x + i); }
	__forceinline float& operator[](int i) { return *(&x + i); }
};


/* Vector Type Constructors */

__device_inline uchar2 make_uchar2(uchar x, uchar y)
{
	uchar2 a = {x, y};
	return a;
}

__device_inline uchar3 make_uchar3(uchar x, uchar y, uchar z)
{
	uchar3 a = {x, y, z};
	return a;
}

__device_inline uchar4 make_uchar4(uchar x, uchar y, uchar z, uchar w)
{
	uchar4 a = {x, y, z, w};
	return a;
}

__device_inline int2 make_int2(int x, int y)
{
	int2 a = {x, y};
	return a;
}

__device_inline int3 make_int3(int x, int y, int z)
{
	int3 a = {x, y, z, 0};

    return a;
}

__device_inline int4 make_int4(int x, int y, int z, int w)
{
	int4 a = {x, y, z, w};

	return a;
}

__device_inline uint2 make_uint2(uint x, uint y)
{
	uint2 a = {x, y};
	return a;
}

__device_inline uint3 make_uint3(uint x, uint y, uint z)
{
	uint3 a = {x, y, z};
	return a;
}

__device_inline uint4 make_uint4(uint x, uint y, uint z, uint w)
{
	uint4 a = {x, y, z, w};
	return a;
}

__device_inline float2 make_float2(float x, float y)
{
	float2 a = {x, y};
	return a;
}

__device_inline float3 make_float3(float x, float y, float z)
{
	float3 a = {x, y, z};

	return a;
}

__device_inline float4 make_float4(float x, float y, float z, float w)
{
	float4 a = {x, y, z, w};

	return a;
}

__device_inline int align_up(int offset, int alignment)
{
	return (offset + alignment - 1) & ~(alignment - 1);
}

__device_inline int3 make_int3(int i)
{
	int3 a = {i, i, i, i};

	return a;
}

__device_inline int4 make_int4(int i)
{
	int4 a = {i, i, i, i};

	return a;
}

__device_inline float3 make_float3(float f)
{
	float3 a = {f, f, f};

	return a;
}

__device_inline float4 make_float4(float f)
{
	float4 a = {f, f, f, f};

	return a;
}

__device_inline float4 make_float4(const int4& i)
{
	float4 a = {(float)i.x, (float)i.y, (float)i.z, (float)i.w};

	return a;
}

__device_inline int4 make_int4(const float3& f)
{
	int4 a = {(int)f.x, (int)f.y, (int)f.z};

	return a;
}

OCT_NAMESPACE_END

#endif /* __UTIL_TYPES_H__ */

