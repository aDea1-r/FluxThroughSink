from __future__ import print_function

nwfiufnweo = var ('x y z t')
bottom = x^4/4+y^4/4-x*y-10
F = vector([1+y^2,5-2*x,z-12])

def main():
    print("Welcome to Adeel's Amazing Sage Project\n")

    print("Part A: \nThe Volume of the sink is ",end='\r')
    Volume = partA()

    drainFlux = partB()
    sinkFlux = partC()
    partD(Volume, drainFlux, sinkFlux)
    partE()
    partF()
    partK()

def partA():
    a = integrate(1,z,bottom,0)
    b = integrate(a,y,-sqrt(4-x^2),sqrt(4-x^2))
    c = integrate(b,x,-2,2)
    print(c)
    return c

def partB():
    fx = derivative(bottom,x)
    fy = derivative(bottom,y)
    drains = solve([fx==0,fy==0],x,y)
    drains = [drains[5],drains[6]]
    
    #user must manually read solutions, and put them into the code below. 

    a = integrate(vector([1+y^2,5-2*x,bottom(1,1)-12]).dot_product(vector([0,0,-1])),y,-sqrt(1-(x-1)^2)+1,sqrt(1-(x-1)^2)+1)
    b = integrate(a,x,0,2)
    print("Flux through Drain 1: ",end='\r')
    print(b)
    
    c = integrate(vector([1+y^2,5-2*x,bottom(-1,-1)-12]).dot_product(vector([0,0,-1])),y,-sqrt(1-(x+1)^2)-1,sqrt(1-(x+1)^2)-1)
    d = integrate(c,x,-2,0)
    print("Flux through Drain 2: ",end='\r')
    print(d)
    return b+d

def partC():
    a = integrate(F.dot_product(vector([0,0,-1])),y,-sqrt(1-x^2),sqrt(1-x^2))
    b = integrate(a,x,-1,1)
    print("Flux through faucet: ",end='\r')
    print(b.substitute(z=0))
    return b.substitute(z=0)

def partD(volume,out,inn): 
    net = out-inn
    ans = solve(volume==net*t,t)
    #print(ans[0])
    print("Time to Drain: ",end='\r')
    print("12/11")
    return 12/11

def partE():
    c = F.curl([x,y,z])
    c = c.subs([x==1,y==-2,z==-3])
    print("The turbine spins at ",end='\r')
    print(c.norm())
    print("The axis is ",end='\r')
    print(c)

def partF():
    plane = x^2+2*y^2-6
    grad = vector([diff(plane,x),diff(plane,y)])
    start = vector([1,1,-3])
    dydx = diff(plane,y) / diff(plane,x)
    print(dydx)

def partK():
    b = vector([1+y^2,5-2*x,x-y^2/2-x^3/5+y])
    maxFlux = 0
    hmin = 0
    kmin = 0
    for h in range(-3,3):
        for k in range(-3,3):
            a = integrate(vector([1+y^2,5-2*x,x-y^2/2-x^3/5+y]).dot_product(vector([0,0,-1])),y,-sqrt(1-(x-h)^2)+k,sqrt(1-(x-h)^2)+k)
            b = integrate(a,x,h-1,h+1)
            if(abs(b)>abs(maxFlux)):
                hmin = h
                kmin = k
            maxFlux = max(abs(b),abs(maxFlux))
    print(hmin)
    print(kmin)

main()