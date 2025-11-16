class EOS_HAchievements(c_void_p):
    # ...
    def CopyAchievementDefinitionV2ByIndex(self, Options, OutDefinition):
        # type: (EOS_HAchievements, POINTER(EOS_Achievements_CopyAchievementDefinitionV2ByIndexOptions), POINTER(POINTER(EOS_Achievements_DefinitionV2))) -> EOS_EResult
        return EOS_Achievements_CopyAchievementDefinitionV2ByIndex(self, Options, OutDefinition)
