import json

class Game_stats():
    """跟踪游戏的统计信息"""
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

        #游戏刚启动时处于非活动状态
        self.game_active = False

        #任何青黄下都不应该重置最高得分
        try:
            with open('high_score.json', 'r') as f_obj:
                self.high_score = json.load(f_obj)
        except json.decoder.JSONDecodeError:
            self.high_score = 0
        except FileNotFoundError:
            self.high_score = 0
            
    def reset_stats(self):
        """初始化在游戏运行间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
