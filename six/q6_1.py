def f(y, t):
    return -y + 1.0


def odestep(f, y, t, dt):
    return y + dt * f(y, t)


if __name__ == '__main__':
    for dt in [0.2, 0.1, 0.02, 0.01]:
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

