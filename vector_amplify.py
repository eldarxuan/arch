    def amplify(self, factor):
        # 向量扩大倍数
        amp_vec = Vector(self.x * factor, self.y * factor, length = self.length * factor)
        return amp_vec