from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Orders,Orderupdate,SellerDetails
from math import ceil
from django.views.decorators.csrf import csrf_exempt
import json
from paytm import checksum
from .form import ImageForm 
MERCHANT_KEY='fO!j#7_jy@U66lX_'
"""username:Amar
    password:Amar123"""
def index(request):
    products=Product.objects.all()
    print(products)
    # n=len(products)
    # nslides=n//4+ceil((n/4-n//4))
    # params={'no_of_slides':nslides,'range':range(1,nslides),'product':products}
    allprods=[]
    catprods=Product.objects.values('category','id')
    # print(catprods)
    cats={item['category'] for item in catprods}
    # print(cats)
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        print(prod)
        n=len(prod)
        nslides=n//4+ceil((n/4)-(n//4))
        
                
        allprods.append([prod,range(1,nslides),nslides])

    # allprods=[[products,range(1,nslides),nslides],
    #             [products,range(1,nslides),nslides]]
    params={'allprods':allprods}
    return render(request,'shop/index.html',params)
def about(request): 
    return render(request,'shop/about.html')
def contact(request):
    if request.method=='POST':
        
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        desc=request.POST.get('desc','')
        phone=request.POST.get('phone','')
        contacts=Contact(name=name,email=email,phone=phone,desc=desc)
        contacts.save()
        than=True
        return render(request,'shop/contact.html',{"than":than})
    return render(request,'shop/contact.html')
def tracker(request):
    if request.method=='POST':
        
        orderid=request.POST.get('orderid','')
        email=request.POST.get('email','')
       
        try:
            order=Orders.objects.filter(order_id=orderid,email=email)
            
            if len(order)>0:
                update=Orderupdate.objects.filter(order_id=orderid)
                updates=[]
                for i in update:
                    updates.append({'text':i.update_desc,'time':i.timestamp})
                    respons=json.dumps({"status":"success","updates":updates,"itemsjson":order[0].items_json},default=str)
                return HttpResponse(respons)
            else:
                return HttpResponse('{"status":"no such item"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')
    
    return render(request,'shop/tracker.html')
def searchmatch(query,i):
    #return true only if query matches the item
    if query in i.desc.lower() or query in i.product_name.lower() or query in i.category.lower():
        return True
    else:
        return False
def search(request):
    query=request.GET.get('search')
    allprods=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    # print(cats)
    for cat in cats:
        
        prodtemp=Product.objects.filter(category=cat)
        prod=[i for i in prodtemp if searchmatch(query,i)]
        n=len(prod)
        nslides=n//4+ceil((n/4)-(n//4))
        
        if len(prod)!=0:
            allprods.append([prod,range(1,nslides),nslides])

    # allprods=[[products,range(1,nslides),nslides],
    #             [products,range(1,nslides),nslides]]
    params={'allprods':allprods,'msg': ""}
    if len(allprods)==0 or len(query)<4:
        params={'msg':"oops!no such result"}
    return render(request,'shop/search.html',params)
def prodview(request,myid):
    #fetfch product from id
    product=Product.objects.filter(id=myid)

    
    return render(request,'shop/prodciew.html',{'product':product[0]})
def checkout(request):
    if request.method=='POST':
        items_json=request.POST.get('itemsJson','')
        name=request.POST.get('name','')
        amount=request.POST.get('amount','')
        email=request.POST.get('email','')
        address=request.POST.get('address1','') + "/" +request.POST.get('address2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip_code','')
        phone_no=request.POST.get('phone_no','')
        order=Orders(items_json=items_json,name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone_no=phone_no,amnt=amount)
        order.save()
        thank=True
        id=order.order_id
        update=Orderupdate(order_id=order.order_id,update_desc='The order has been place')
        update.save()
        
        # return render(request,'shop/checkout.html',{'thank':thank,'id':id})
        # request payttm to transfer the amount to ur account  after payment by user
        param_dict={
                'MID':'aPtxBs22076670920236',
                'ORDER_ID': str(order.order_id),
                'TXN_AMOUNT': str(amount),
                'CUST_ID': email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',
        }
        param_dict['CHECKSUMHASH']=checksum.generate_checksum(param_dict,MERCHANT_KEY)
        return render(request,'shop/paytm.html',{'param_dict':param_dict})
    return render(request,'shop/checkout.html')
@csrf_exempt
def handlereq(request):
    #paytm will send u post request here    
    return HttpResponse('done')
def Exchange(request):
    #paytm will send u post request here    
    return render(request,'shop/Exchange.html')
   
    
def Exchange_sell(request):
    if request.method=='POST':
        # print(request.POST.get('bookname'),request.POST.get('latt'))
        selldetails=SellerDetails(request.POST,request.FILES)
        bookname=request.POST.get('bookname','')
        bookauthor=request.POST.get('bookauthor','')
        bookcategory=request.POST.get('bookcategory','')
        usedtime=request.POST.get('usedtime','')
        title=request.POST.get('title','')
        price=request.POST.get('price','')
        city=request.POST.get('city','')
        longi=request.POST.get('long',"")
        latt=request.POST.get('latt',"")
        img1=request.FILES.get("img1")
        img2=request.FILES.get("img2")
        sell_detail=SellerDetails(bookname=bookname,bookauthor=bookauthor,bookcategory=bookcategory,usedtime=usedtime,title=title,price=price,longi=longi,latt=latt,city=city,img1=img1,img2=img2)
        sell_detail.save()

        # print(img1,img2)
        than=True
        return render(request,'shop/Exchange_sell.html',{"than":than})
    #paytm will send u post request here    
    return render(request,'shop/Exchange_sell.html')
def Exchange_buy(request):
    

    #paytm will send u post request here    
    return render(request,'shop/Exchange_buy.html')
def Searches(request):
    if request.method=='GET':
        bookname=request.GET.get("search")
        
       
        list_to_show=[]
        sell_sort_loc=[]
        selleralldet=SellerDetails.objects.all()
       
        # print(float(longi))
        for i in range(len(selleralldet)):
            if bookname.lower() in selleralldet[i].bookname.lower():
                
                list_to_show.append(selleralldet[i])
                print(selleralldet[i].bookname)
            
        #     if float(latt) in range (float(sell_latt[i]['latt'])-0.05,float(sell_latt[i]['latt'])+0.05) and float(longi) in range (float(sell_latt[i]['longi'])-0.05,float(sell_latt[i]['longi'])-0.05):
        #         print(sell_latt)
        #     else:
        #         pass
                
        # if int(sell_long) in range(int(longi)-1):
        #     print(selldet[0])

        # for i in range(len(selldet)):
        #     if selldet[0].lower()==bookname.lower():
        #         list_to_show.append(bookname)
        # selllongi=SellerDetails.objects.values("longi")
        # selllatt=SellerDetails.objects.values("latt")
        # print(bookname,bookcat,bookauth,longi,latt)
        return render(request,'shop/Exchange_Searches.html',{'allitem':list_to_show,"no":len(list_to_show)})
    else:
        return HttpResponse("Method not allowed")
def Exchange_buy_item(request,search,id):
    item=SellerDetails.objects.filter(bookname=search,seller_id=id)
    print(item[0])
    return render(request,"itemdetails.html",{"item":item[0]})
