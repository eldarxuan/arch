    def unit(self):
        # 单位化一个向量
        unit_vec = Vector(self.x/self.length, self.y/self.length, length = 1.0)
        return unit_vec