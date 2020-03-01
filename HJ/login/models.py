from django.db import models

class hj_user(models.Model):
	name = models.CharField(max_length=10)
	password = models.CharField(max_length=8)

class orders(models.Model):
	orderid = models.CharField(max_length=9)  # 产品批次id
	number = models.IntegerField()  # 订单号
	name = models.CharField(max_length=100)  # 客户名称
	product_type = models.CharField(max_length=10)  # 产品型号
	color = models.CharField(max_length=6)  # 产品颜色
	count = models.IntegerField()  # 产品数量
	submit_user = models.ForeignKey(hj_user, on_delete=models.SET_DEFAULT, default='离职')