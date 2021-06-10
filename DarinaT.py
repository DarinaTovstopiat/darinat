def Dichotomy(a, b, eps):
    delta = eps/10
    k = 0
    y = (a + b - delta)/2
    z = (a + b + delta)/2
    while np.abs(b-a) > eps:
        if f(y) <= f(z):
            b = z
        else:
            a = y
        y = (a + b - delta)/2
        z = (a + b + delta)/2
        k += 1
    xmin = (a + b)/2
    fmin = f(xmin)
    return xmin, fmin, k



def GoldenRatio(a, b, eps):
    k = 0
    fi = 1.618
    while np.abs(a - b) > eps:
        k += 1
        y = b - (b - a)/fi
        z = a + (b - a)/fi
        if f(y) <= f(z):
            b = z
            z = y
            y = b - (b - a)/fi
        else:
            a = y
            y = z
            z = a + (b - a)/fi
    xmin = (a + b)/2
    fmin = f(xmin)
    return xmin, fmin, k



def QuadraticApprox(a, b, eps):
    x1 = a
    x2 = b
    h = eps - eps/10
    k = 0
    if f(x1) > f(x2):
        x3 = x1 + 2*h
    else:
        x3 = x1 - h
    L = sorted([[f(x1), x1], [f(x2), x2], [f(x3), x3]])
    fmin = L[0][0]
    xmin = L[0][1]
    a0 = f(x1)
    a1 = (f(x2) - f(x1))/(x2 - x1)
    a2 = 1/(x3 - x2)*((f(x3) - f(x1))/(x3 - x1) - (f(x2) - f(x1))/(x2 - x1))
    xx = (x2 + x1)/2 - a1/(2*a2)
    while np.abs(xx - xmin) > eps:
        if f(xx) < fmin:
            x1 = xx
        else:
            x1 = xmin
        x2 = x1 + h
        if f(x1) > f(x2):
            x3 = x1 + 2*h
        else:
            x3 = x1 - h
        L = sorted([[f(x1), x1], [f(x2), x2], [f(x3), x3]])
        fmin = L[0][0]
        xmin = L[0][1]
        a0 = f(x1)
        a1 = (f(x2) - f(x1))/(x2 - x1)
        a2 = 1/(x3 - x2)*((f(x3) - f(x1))/(x3 - x1) - (f(x2) - f(x1))/(x2 - x1))
        xx = (x2 + x1)/2 - a1/(2*a2)
        k += 1
    return xx, f(xx), k



def MidpointMethod(a, b, eps):
    k = 0
    midpoint = (a + b)/2
    d_fx = df(midpoint)
    while np.abs(d_fx) > eps:
        if d_fx > 0:
            b = midpoint
        else:
            a = midpoint
        midpoint = (a + b)/2
        d_fx = df(midpoint)
        k += 1
    return midpoint, f(midpoint), k




def ChordMethod(a, b, eps):
    k = 0
    d_afx = df(a)
    d_bfx = df(b)
    xx = a - (d_afx/(d_afx - d_bfx))*(a - b)
    d_fx = df(xx)
    while np.abs(d_fx) > eps:
        if d_fx > 0:
            b = xx
            d_bfx = d_fx
            k += 1
        else:
            a = xx
            d_afx = d_fx
            k += 1
        xx = a - (d_afx/(d_afx - d_bfx))*(a - b)
        d_fx = df(xx)
    x_min = xx
    f_min = f(x_min)
    return x_min, f_min, k




def NewtonMethod(a, b, eps):
    x0 = a
    d_fx = df(x0)
    dd_fx = ddf(x0)
    x1 = x0 - d_fx/dd_fx
    d_fx1 = df(x1)
    if np.abs(d_fx) < eps:
        x_min = x0
        f_min = f(x_min)
    else:
        k = 0
        while np.abs(d_fx1) > eps:
            x0 = x1
            d_fx = df(x0)
            dd_fx = ddf(x0)
            x1 = x0 - d_fx/dd_fx
            d_fx1 = df(x1)
            k += 1
        x_min = x1
        f_min = f(x_min)
    return x_min, f_min, k




def SA(x):
    k=1
    T0=10
    Tend=10**(-6)
    r=0.95
    a=-10
    b=10
    E=f(x)
    T=T0
    while T>Tend and k<1000:
        x_new=x+T*np.array([rnd.uniform(a,b), rnd.uniform(a,b)])
        E_new=f(x_new)
        deltaE=E_new-E
        if deltaE<0:
            x=x_new
            E=E_new
            k+=1
            T=r*T
        else:
            p=np.exp(-deltaE/T)
            alpha=rnd.random()
            if alpha<p:
                x=x_new
                E=E_new
                k+=1
                T=r*T
    return [x_new, E_new, k]



def PSO(s, d):
    xmin=-10
    xmax=10
    tmax=50

    x=np.zeros((s, d))
    v=np.zeros((s, d))
    p=np.zeros((s, d))

    fitness=np.zeros(s)
    fp=np.zeros(s)

    w=1/(2*np.log(2))   
    c1=0.5+np.log(2)
    c2=0.5+np.log(2)

    for i in range(s):
        for j in range(d):
            x[i][j]=uniform(xmin, xmax)
            v[i][j]=(uniform(xmin, xmax)-x[i][j])/2
            p[i][j]=x[i][j]
        fitness[i]=f(x[i])
        fp[i]=fitness[i]

    gbest = 1 
    for i in range(1, s):
        if fp[i]<fp[gbest]:
            gbest = i

    for t in range(tmax):
        for i in range(s):
            for j in range(d):
                r1=random()
                r2=random()

                v[i][j]=w*v[i][j]+c1*r1*(p[i][j]-x[i][j])

                if (i != gbest):
                    v[i][j]=v[i][j]+c2*r2*(p[gbest][j]-x[i][j])

                x[i][j]=x[i][j]+v[i][j]

                if x[i][j]<xmin:
                    x[i][j]=xmin
                    v[i][j]=0

                if x[i][j]>xmax:
                    x[i][j]=xmax
                    v[i][j]=0

    for i in range(s):
        fitness[i]=f(x[i])
        if fitness[i]<fp[i]:
            fp[i]=fitness[i]
            for j in range(d):
                p[i][j]=x[i][j]

    for i in range (s):
        if fp[i]<fp[gbest]:
            gbest = i

    x_min = fp[gbest]
    f_min = p[gbest]

    return (x_min, f_min)



def GNO(d):
    n = 20
    tmax = 100
    t = 0
    lb = -5
    rb = 5
    
    x = np.zeros((n,d))
    F = np.zeros((n,1))
    
    x_alpha = np.zeros(d)
    F_alpha = np.inf
    
    x_beta = np.zeros(d)
    F_beta = np.inf
    
    x_delta = np.zeros(d)
    F_delta = np.inf
    
    for i in range(n):
        x[i] = lb + (rb - lb)*random()
        
    while t<tmax:
        for i in range(n):
            F[i] = f(x[i])
            if F[i]<F_alpha:
                F_alpha = F[i]
                x_alpha = x[i]
            if F[i]>F_alpha and F[i]<F_beta:
                F_beta = F[i]
                x_beta = x[i]
            if F[i]>F_alpha and F[i]>F_beta and F[i]<F_delta:
                F_delta = F[i]
                x_delta = x[i]
        a = 2-t*(2/tmax)
        for i in range(n):
            for j in range(d):
                r1 = random()
                r2 = random()
                A1 = 2*a*r1-a
                C1 = 2*r2
                
                D_alpha = np.abs(C1*x_alpha[j]-x[i][j])
                X1 = x_alpha[j]-A1*D_alpha
                
                r1 = random()
                r2 = random()
                A2 = 2*a*r1-a
                C2 = 2*r2
                
                D_beta = np.abs(C2*x_beta[j]-x[i][j])
                X2 = x_beta[j]-A2*D_beta
                
                r1 = random()
                r2 = random()
                A3 = 2*a*r1-a
                C3 = 2*r2
                
                D_delta = np.abs(C3*x_delta[j]-x[i][j])
                X3 = x_delta[j]-A3*D_delta
                
                x[i][j] = (X1+X2+X3)/3
                
        t += 1
        return (x_alpha, F_alpha)






