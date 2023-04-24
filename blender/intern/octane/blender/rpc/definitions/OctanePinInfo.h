// clang-format off
#ifndef __OCTANE_PIN_INFO_H__
#define __OCTANE_PIN_INFO_H__
#include "OctaneBase.h"

#ifndef OCTANE_SERVER
/// Result of compiling code
namespace Octane {
	enum CompilationResult
	{
		/// not compiled yet
		COMPILE_NONE = 0,
		/// Compilation succeeded
		COMPILE_SUCCESS = 1,
		/// Compilation failed
		COMPILE_FAILED = 2
	};
}
#else
#endif

MSGPACK_ADD_ENUM(Octane::CompilationResult);

namespace OctaneDataTransferObject {

	/// Stores static information for pins of type PT_BOOL.
	struct ApiBoolPinInfo
	{
		bool mDefaultValue;
		ApiBoolPinInfo& operator=(const ApiBoolPinInfo& other) { if (&other != this) { mDefaultValue = other.mDefaultValue; } return *this; }
#ifdef OCTANE_SERVER
		ApiBoolPinInfo& operator=(const Octane::ApiBoolPinInfo& other) { mDefaultValue = other.mDefaultValue; return *this; }
#endif
		MSGPACK_DEFINE(mDefaultValue);
	};

	/// Stores static information for pins of type PT_FLOAT.
	struct ApiFloatPinInfo
	{
		/// The basic data type that is used for float pins and their defaults.
		typedef OctaneDataTransferObject::float_3 DataT;

		/// The maximum dimension of the data that can be read through a float pin.
		static const uint8_t MAX_DIMS = DataT::DIM_COUNT;

		/// Describes the properties of one dimension.
		struct DimInfo
		{
			std::string mName;
			float		mMinValue;
			float		mMaxValue;
			float		mSliderMinValue;
			float		mSliderMaxValue;
			float		mSliderStep;
			ApiFloatPinInfo::DimInfo& operator=(const ApiFloatPinInfo::DimInfo& other) {
				if (&other != this) { mName = other.mName; mMinValue = other.mMinValue; mMaxValue = other.mMaxValue; mSliderMinValue = other.mSliderMinValue; mSliderMaxValue = other.mSliderMaxValue; mSliderStep = other.mSliderStep; }
				return *this;
			}
#ifdef OCTANE_SERVER
			ApiFloatPinInfo::DimInfo& operator=(const Octane::ApiFloatPinInfo::DimInfo& other) { 
				mName = other.mName ? other.mName : ""; mMinValue = other.mMinValue; mMaxValue = other.mMaxValue; mSliderMinValue = other.mSliderMinValue; mSliderMaxValue = other.mSliderMaxValue; mSliderStep = other.mSliderStep;
				return *this;
			}
#endif
			MSGPACK_DEFINE(mName, mMinValue, mMaxValue, mSliderMinValue, mSliderMaxValue, mSliderStep);
		};

		/// The number of dimensions the pin requires (up to 3).
		uint8_t mDimCount;
		/// The dimension descriptions.
		DimInfo mDimInfos[MAX_DIMS];
		/// The default value of the pin.
		DataT   mDefaultValue;
		/// TRUE if the user interface should use sliders for this pin.
		bool    mUseSliders;
		/// TRUE if the user interface should allow a logarithmic slider interface.
		bool    mAllowLog;
		/// TRUE if the user interface should use a logarithmic slider interface (if possible).
		bool    mDefaultIsLog;
		/// TRUE if the user interface display percentages
		bool    mDisplayPercentages;
		/// TRUE if the user interface should allow changes to all three components which keep the
		/// aspect ratio.
		bool    mUseAspectRatio;
		/// TRUE if a colour swatch should be displayed.
		bool    mIsColor;

		ApiFloatPinInfo& operator=(const ApiFloatPinInfo& other) {
			if (&other != this) {
				mDimCount = other.mDimCount; mDefaultValue = other.mDefaultValue; mUseSliders = other.mUseSliders; mAllowLog = other.mAllowLog; mDefaultIsLog = other.mDefaultIsLog; mDisplayPercentages = other.mDisplayPercentages; mUseAspectRatio = other.mUseAspectRatio; mIsColor = other.mIsColor;
				for (int i = 0; i < MAX_DIMS; ++i) { mDimInfos[i] = other.mDimInfos[i];  }				
			}
			return *this;
		}
#ifdef OCTANE_SERVER
		ApiFloatPinInfo& operator=(const Octane::ApiFloatPinInfo& other) { 
			mDimCount = other.mDimCount; mDefaultValue = other.mDefaultValue; mUseSliders = other.mUseSliders; mAllowLog = other.mAllowLog; mDefaultIsLog = other.mDefaultIsLog; mDisplayPercentages = other.mDisplayPercentages; mUseAspectRatio = other.mUseAspectRatio; mIsColor = other.mIsColor;
			for (int i = 0; i < MAX_DIMS; ++i) { mDimInfos[i] = other.mDimInfos[i]; }
			return *this;
		}
#endif
		MSGPACK_DEFINE(mDimCount, mDimInfos, mDefaultValue, mUseSliders, mAllowLog, mDefaultIsLog, mDisplayPercentages, mUseAspectRatio, mIsColor);
	};


	/// Stores static information for pins of type PT_INT.
	struct ApiIntPinInfo
	{
		/// The basic data type that is used for int pins and their defaults.
		typedef OctaneDataTransferObject::int32_3 DataT;

		/// The maximum dimension of the data that can be read through an int pin.
		static const uint8_t MAX_DIMS = DataT::DIM_COUNT;

		/// Describes the properties of one dimension.
		struct DimInfo
		{
			std::string mName;
			int32_t		mMinValue;
			int32_t		mMaxValue;
			int32_t		mSliderMinValue;
			int32_t		mSliderMaxValue;
			int32_t		mSliderStep;

			ApiIntPinInfo::DimInfo& operator=(const ApiIntPinInfo::DimInfo& other) {
				if (&other != this) { mName = other.mName; mMinValue = other.mMinValue; mMaxValue = other.mMaxValue; mSliderMinValue = other.mSliderMinValue; mSliderMaxValue = other.mSliderMaxValue; mSliderStep = other.mSliderStep; }
				return *this;
			}
#ifdef OCTANE_SERVER
			ApiIntPinInfo::DimInfo& operator=(const Octane::ApiIntPinInfo::DimInfo& other) {
				mName = other.mName ? other.mName : ""; mMinValue = other.mMinValue; mMaxValue = other.mMaxValue; mSliderMinValue = other.mSliderMinValue; mSliderMaxValue = other.mSliderMaxValue; mSliderStep = other.mSliderStep;
				return *this;
			}
#endif
			MSGPACK_DEFINE(mName, mMinValue, mMaxValue, mSliderMinValue, mSliderMaxValue, mSliderStep);
		};

		/// The number of dimensions the pin requires (up to 3).
		uint8_t mDimCount;
		/// The dimension descriptions.
		DimInfo mDimInfos[MAX_DIMS];
		/// Teh default value of the pin.
		DataT   mDefaultValue;
		/// TRUE if the user interface should use sliders for this pin.
		bool    mUseSliders;
		/// TRUE if the user interface should allow a logarithmic slider interface.
		bool    mAllowLog;
		/// TRUE if the user interface should use a logarithmic slider interface (if possible).
		bool    mDefaultIsLog;
		/// TRUE if a colour swatch should be displayed.
		bool    mIsColor;

		ApiIntPinInfo& operator=(const ApiIntPinInfo& other) {
			if (&other != this) {
				mDimCount = other.mDimCount; mDefaultValue = other.mDefaultValue; mUseSliders = other.mUseSliders; mAllowLog = other.mAllowLog; mDefaultIsLog = other.mDefaultIsLog; mIsColor = other.mIsColor;
				for (int i = 0; i < MAX_DIMS; ++i) { mDimInfos[i] = other.mDimInfos[i]; }
			}
			return *this;
		}
#ifdef OCTANE_SERVER
		ApiIntPinInfo& operator=(const Octane::ApiIntPinInfo& other) {
			mDimCount = other.mDimCount; mDefaultValue = other.mDefaultValue; mUseSliders = other.mUseSliders; mAllowLog = other.mAllowLog; mDefaultIsLog = other.mDefaultIsLog; mIsColor = other.mIsColor;
			for (int i = 0; i < MAX_DIMS; ++i) { mDimInfos[i] = other.mDimInfos[i]; }
			return *this;
		}
#endif
		MSGPACK_DEFINE(mDimCount, mDimInfos, mDefaultValue, mUseSliders, mAllowLog, mDefaultIsLog, mIsColor);
	};


	/// Stores static information for pins of type PT_ENUM.
	struct ApiEnumPinInfo
	{
		/// Represents an enum value identified by some meaningful name.
		struct Value
		{
			/// Actual enumeration value.
			int32_t     mValue;
			/// Label of the enumeration value.
			std::string mLabel;
			Value& operator=(const Value& other) { if (&other != this) { mValue = other.mValue; mLabel = other.mLabel; } return *this; }
#ifdef OCTANE_SERVER
			Value& operator=(const Octane::ApiEnumPinInfo::Value& other) { mValue = other.mValue; other.mLabel ? other.mLabel : ""; return *this; }
			void set(const Octane::ApiEnumPinInfo::Value& other) { mValue = other.mValue; mLabel = other.mLabel ? other.mLabel : ""; }
#endif
			MSGPACK_DEFINE(mValue, mLabel);
		};

		/// Array of the enum values (Can be NULL).
		std::vector<Value>	mValues;
		/// Number of enum values.
		uint32_t			mValueCount;
		/// Default enum value.
		int32_t				mDefaultValue;
		ApiEnumPinInfo& operator=(const ApiEnumPinInfo& other) { if (&other != this) { mValues = other.mValues;  mValueCount = other.mValueCount; mDefaultValue = other.mDefaultValue; } return *this; }
#ifdef OCTANE_SERVER
		ApiEnumPinInfo& operator=(const Octane::ApiEnumPinInfo& other) { 						
			for (int i = 0; i < other.mValueCount; ++i) {				
				ApiEnumPinInfo::Value value;
				value.set(*(other.mValues + i));
				mValues.push_back(value); 
			}
			mValueCount = other.mValueCount; mDefaultValue = other.mDefaultValue;  
			return *this; 
		}
#endif
		MSGPACK_DEFINE(mValues, mValueCount, mDefaultValue);
	};

	/// Stores static information for pins of type PT_TEXTURE.
	struct ApiTexturePinInfo
	{
		/// The basic data type that is used for texture node values.
		typedef OctaneDataTransferObject::float_3 DataT;

		/// The minimum value the pin accepts.
		float mMinValue;
		/// The maximum value the pin accepts.
		float mMaxValue;
		/// The minimum slider value that should be displayed for texture nodes connected with this pin.
		float mSliderMinValue;
		/// The maximum slider value that should be displayed for texture nodes connected with this pin.
		float mSliderMaxValue;
		/// The default RGB values of the texture pin. 
		/// Float texture pins have all three components set to the same value.
		DataT mDefaultValue;
		/// Set to TRUE if the pin is used to fetch a spectrum.
		/// FALSE if we only need a float texture.
		/// Only makes sense for texture pins of material/emitter/medium nodes.
		bool  mUsesSpectrum;

		ApiTexturePinInfo& operator=(const ApiTexturePinInfo& other) { if (&other != this) { mMinValue = other.mMinValue; mMaxValue = other.mMaxValue; mSliderMinValue = other.mSliderMinValue; mSliderMaxValue = other.mSliderMaxValue; mDefaultValue = other.mDefaultValue; mUsesSpectrum = other.mUsesSpectrum; } return *this; }
#ifdef OCTANE_SERVER
		ApiTexturePinInfo& operator=(const Octane::ApiTexturePinInfo& other) { mMinValue = other.mMinValue; mMaxValue = other.mMaxValue; mSliderMinValue = other.mSliderMinValue; mSliderMaxValue = other.mSliderMaxValue; mDefaultValue = other.mDefaultValue; mUsesSpectrum = other.mUsesSpectrum; return *this; }
#endif
		MSGPACK_DEFINE(mMinValue, mMaxValue, mSliderMinValue, mSliderMaxValue, mDefaultValue, mUsesSpectrum);
	};

	/// Stores static information for pins of type PT_TRANSFORM.
	struct ApiTransformPinInfo
	{
		/// Represents transformation value boundaries used for the UI.
		struct Bounds
		{
			double mDefaultValue;
			double mMinValue;
			double mMaxValue;
			ApiTransformPinInfo::Bounds& operator=(const ApiTransformPinInfo::Bounds& other) { if (&other != this) { mDefaultValue = other.mDefaultValue; mMinValue = other.mMinValue; mMaxValue = other.mMaxValue; } return *this; }
#ifdef OCTANE_SERVER
			ApiTransformPinInfo::Bounds& operator=(const Octane::ApiTransformPinInfo::Bounds& other) { mDefaultValue = other.mDefaultValue; mMinValue = other.mMinValue; mMaxValue = other.mMaxValue; return *this; }
#endif
			MSGPACK_DEFINE(mDefaultValue, mMinValue, mMaxValue);
		};

		/// The default value for this pin
		OctaneDataTransferObject::MatrixF mDefaultValue;
		/// The dimension of the transformation.
		uint8_t         mDimCount;
		/// Boundaries for the scale values in the UI.
		Bounds          mScaleBounds;
		/// Boundaries for the rotation values (in degrees) in the UI.
		Bounds          mRotationBounds;
		/// Boundaries for the translation values in the UI.
		Bounds          mTranslationBounds;

		ApiTransformPinInfo& operator=(const ApiTransformPinInfo& other) { if (&other != this) { mDefaultValue = other.mDefaultValue; mDimCount = other.mDimCount; mScaleBounds = other.mScaleBounds; mRotationBounds = other.mRotationBounds; mTranslationBounds = other.mTranslationBounds; } return *this; }
#ifdef OCTANE_SERVER
		ApiTransformPinInfo& operator=(const Octane::ApiTransformPinInfo& other) { mDefaultValue = other.mDefaultValue; mDimCount = other.mDimCount; mScaleBounds = other.mScaleBounds; mRotationBounds = other.mRotationBounds; mTranslationBounds = other.mTranslationBounds; return *this; }
#endif
		MSGPACK_DEFINE(mDefaultValue, mDimCount, mScaleBounds, mRotationBounds, mTranslationBounds);
	};


	/// Stores static information for pins of type PT_STRING.
	struct ApiStringPinInfo
	{
		/// The default text in this node pin
		std::string					mDefaultValue;
		/// if mIsFile is true, this text gives the file name patterns, separated by a semicolon (;)
		std::string					mFilePatterns;
		/// List of values to choose from.
		std::vector<std::string>	mValues;
		/// Amount of values
		size_t						mValueCount;
		/// if mIsFile is false and mMultiLine is true, this should allow entry of multiple lines of
		/// text.
		bool						mMultiLine;
		/// if true the interface should allow browsing for a file
		bool						mIsFile;
		/// if true the interface should allow browsing for a file which doesn't exist yet.
		bool						mForSaving;
		/// if a list of values is given, determines if users may enter a value which is not in
		/// the list.
		bool						mAllowCustomValue;
		ApiStringPinInfo& operator=(const ApiStringPinInfo& other) { if (&other != this) { mDefaultValue = other.mDefaultValue; mFilePatterns = other.mFilePatterns; mValues = other.mValues; mValueCount = other.mValueCount; mMultiLine = other.mMultiLine; mIsFile = other.mIsFile; mForSaving = other.mForSaving; mAllowCustomValue = other.mAllowCustomValue; } return *this; }
#ifdef OCTANE_SERVER
		ApiStringPinInfo& operator=(const Octane::ApiStringPinInfo& other) { 
			for (int i = 0; i < other.mValueCount; ++i) {
				mValues.push_back(other.mValues[i]);
			}
			mDefaultValue = other.mDefaultValue ? other.mDefaultValue : "";
			mFilePatterns = other.mFilePatterns ? other.mFilePatterns : "";
			mValueCount = other.mValueCount; mMultiLine = other.mMultiLine; mIsFile = other.mIsFile; mForSaving = other.mForSaving; mAllowCustomValue = other.mAllowCustomValue;
			return *this; 
		}
#endif
		MSGPACK_DEFINE(mDefaultValue, mFilePatterns, mValues, mValueCount, mMultiLine, mIsFile, mForSaving, mAllowCustomValue);
	};

	/// Stores static information of a particular pin.
	struct ApiNodePinInfo
	{
		Octane::NodePinType			mType;
		std::string					mName;
		std::string					mLabelName;
		ApiBoolPinInfo				mBoolInfo;
		ApiFloatPinInfo				mFloatInfo;
		ApiIntPinInfo				mIntInfo;
		ApiEnumPinInfo				mEnumInfo;
		ApiTexturePinInfo			mTexInfo;
		ApiTransformPinInfo			mTransformInfo;
		ApiStringPinInfo			mStringInfo;
		bool						mIsOutput;
		bool						mUseStrValue;
		std::string					mDefaultStrValue;
#ifdef OCTANE_SERVER
		void set(const Octane::ApiNodePinInfo& other, const std::string name, const std::string labelName) {
			switch (other.mType) {
			case Octane::PT_BOOL:
				mBoolInfo = *other.mBoolInfo;
				break;
			case Octane::PT_FLOAT:
				mFloatInfo = *other.mFloatInfo;
				break;
			case Octane::PT_INT:
				mIntInfo = *other.mIntInfo;
				break;
			case Octane::PT_ENUM:
				mEnumInfo = *other.mEnumInfo;
				break;
			case Octane::PT_TEXTURE:
				mTexInfo = *other.mTexInfo;
				break;
			case Octane::PT_TRANSFORM:
				mTransformInfo = *other.mTransformInfo;
				break;
			case Octane::PT_STRING:
				mStringInfo = *other.mStringInfo;
				break;
			default:
				break;
			}
			mName = name;
			mLabelName = labelName;
			mUseStrValue = false;
			mDefaultStrValue = "";
			mType = other.mType;
			mIsOutput = false;
		}
#endif
		MSGPACK_DEFINE(mType, mName, mLabelName, mBoolInfo, mFloatInfo, mIntInfo, mEnumInfo, mTexInfo, mTransformInfo, mStringInfo, mIsOutput, mUseStrValue, mDefaultStrValue);
	};

	struct OSLNodePinInfo
	{
		std::vector<ApiNodePinInfo>	mPinInfos;

		uint32_t size() { return mPinInfos.size(); }
		ApiNodePinInfo& get_param(uint32_t idx) { return mPinInfos[idx]; }
		void push_back(ApiNodePinInfo& pinInfo) { mPinInfos.push_back(pinInfo); }
		MSGPACK_DEFINE(mPinInfos);
	};
}
#endif
// clang-format on
