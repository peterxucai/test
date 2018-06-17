def index(request):
    return render(request,'index.html')

def goods(request):
    return render(request,'goods.html')

def order(request):
    return render(request,'order.html')

def cart(request):
    return render(request,'cart.html')

