from django.db import models

# Create your models here.
class Product(models.Model):
    product_id =models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")
    def __str__(self):
        return self.product_name
class Contact(models.Model):
    msg_id =models.AutoField(primary_key=True)
    name=models.CharField(max_length=70)
    email=models.CharField(max_length=70,default="")
    desc=models.CharField(max_length=500,default="")
    phone=models.CharField(max_length=500,default="")
    
    def __str__(self):
        return self.name
class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    amnt=models.IntegerField(default=0)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=90)
    address=models.CharField(max_length=290)
    city=models.CharField(max_length=90)
    state=models.CharField(max_length=90)
    zip_code=models.CharField(max_length=90)
    phone_no=models.CharField(max_length=90)
class Orderupdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=5000)
    timestamp=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.update_desc[0:7] + "..."
class SellerDetails(models.Model):
    seller_id=models.AutoField(primary_key=True)
    bookname=models.CharField(max_length=50)
    bookauthor=models.CharField(max_length=50)
    bookcategory=models.CharField(max_length=50)
    usedtime=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    longi=models.CharField(max_length=50)
    latt=models.CharField(max_length=50)
    location=models.CharField(max_length=50,default="")
    img1=models.ImageField(upload_to="shop/images",null=True,blank=True)
    img2=models.ImageField(upload_to="shop/images",null=True,blank=True)


    


