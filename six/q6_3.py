def f(y, t):
    return -y + 1.0


def odestep(f, y, t, dt):
    dA = f(y, t)
    Bpr = y + dt * f(y, t)
    Bpry = f(Bpr, t)
    return y + 0.5 * (dA + Bpry) * dt


if __name__ == '__main__':
    flag = True
    dt = 0.2
    a = [0.6292601568, 0.6314590151664482]
    b = [0.8625519686640395, 0.8641775424979157]
    t = 0
    y = 0
    tf = 2.0
    while abs(a[-1] - a[-2]) > 1.0e-6 and abs(b[-1] - b[-2]) >= 1.0e-6:
        nsteps = int(tf / dt)
        print('when dt is', dt)
        for i in range(nsteps):
            y = odestep(f, y, t, dt)
            t = (i + 1) * dt
            if t == 1.0:
                a.append(y)
                print(t, a[-1])
            elif t == 2.0:
                b.append(y)
                print(t, b[-1])
        dt = dt / 2

    if flag:
        for dt in [0.2, 0.1, 0.05, 0.025, 0.02, 0.01, 0.0015625]:
            t = 0
            y = 0
            tf = 2.0
            nsteps = int(tf / dt)
            print('when dt is', dt)
            for i in range(nsteps):
                y = odestep(f, y, t, dt)
                t = (i + 1) * dt
                if t == 1.0 or t == 2.0:
                    print(t, y)
