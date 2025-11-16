/**
 * Fetches an achievement definition from a given index.
 *
 * @param Options Structure containing the index being accessed
 * [...]
 */
EOS_DECLARE_FUNC(EOS_EResult) EOS_Achievements_CopyAchievementDefinitionV2ByIndex(EOS_HAchievements Handle, const EOS_Achievements_CopyAchievementDefinitionV2ByIndexOptions* Options, EOS_Achievements_DefinitionV2 ** OutDefinition);
