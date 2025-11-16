class EOS_Achievements_CopyAchievementDefinitionV2ByIndexOptions(Structure):
    _pack_ = PACK
    _fields_ = [
        ('ApiVersion', c_int32),
        ('AchievementIndex', c_uint32),
    ]
    def __init__(self, ApiVersion = EOS_ACHIEVEMENTS_COPYACHIEVEMENTDEFINITIONV2BYINDEX_API_LATEST, AchievementIndex = 0):
        Structure.__init__(self, ApiVersion = ApiVersion, AchievementIndex = AchievementIndex)
