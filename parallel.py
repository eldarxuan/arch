    def isVectorParallel(self, vec):
        # 判断实例向量和vec之间是否平行
		if self.cross(self,vec) == 0:
		    return True
		else:
		    return False
			
			
			
			
			
    def isParallel(self):
        # 根据向量计算两个矩形是否平行
        parallel = False
        if self.rec1.vec_lst[0].isVectorParallel(self.rec2.vec_lst[0]) == True:
		    parallel = True
        return parallel