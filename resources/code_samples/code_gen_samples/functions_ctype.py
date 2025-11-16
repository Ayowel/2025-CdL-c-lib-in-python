def not_ready(*args): # type: (...) -> Any
    raise RuntimeError("Please call epic_eos.cdefs.load() before this function.")

EOS_Achievements_CopyAchievementDefinitionV2ByIndex = not_ready

def load(dll):
    global EOS_Achievements_CopyAchievementDefinitionV2ByIndex
    EOS_Achievements_CopyAchievementDefinitionV2ByIndex = dll.EOS_Achievements_CopyAchievementDefinitionV2ByIndex
    EOS_Achievements_CopyAchievementDefinitionV2ByIndex.argtypes = [EOS_HAchievements, POINTER(EOS_Achievements_CopyAchievementDefinitionV2ByIndexOptions), POINTER(POINTER(EOS_Achievements_DefinitionV2))]
    EOS_Achievements_CopyAchievementDefinitionV2ByIndex.restype = EOS_EResult
