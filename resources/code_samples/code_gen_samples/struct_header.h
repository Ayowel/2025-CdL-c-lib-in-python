/**
 * Input parameters for the EOS_Achievements_CopyAchievementDefinitionByIndex function.
 */
EOS_STRUCT(EOS_Achievements_CopyAchievementDefinitionV2ByIndexOptions, (
	/** API Version: Set this to EOS_ACHIEVEMENTS_COPYACHIEVEMENTDEFINITIONV2BYINDEX_API_LATEST. */
	int32_t ApiVersion;
	/** Index of the achievement definition to retrieve from the cache. */
	uint32_t AchievementIndex;
));
