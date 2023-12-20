s = '''%dj -> fj, jn
%xz -> cm
%fn -> rj
%fv -> nt, zp
%ls -> ph, cf
%rk -> zp, tp
&jn -> km, cr, vz
%nh -> ph, ls
%tx -> gb
%xg -> dv, zp
%tp -> gx
&zp -> kj, kz, gx, fv, lv, tp
&gq -> rx
%fj -> sl, jn
%cr -> vz, jn
%rt -> fn, mf
%kj -> tt
%tk -> mg, ph
%xt -> jn, gh
%qx -> bx
%lv -> sx
%nz -> dp, ph
%sx -> kj, zp
%dd -> bf
%gb -> jp
%bj -> ph, nn
%sk -> mf
%bx -> tx, mf
%mt -> xg, zp
%vz -> hf
%vx -> mf, sk
%tt -> mt, zp
%br -> jn, fk
&xj -> gq
%mg -> ph, ps
%nt -> zp, rk
&qs -> gq
%rj -> qx, mf
%bf -> vx, mf
&kz -> gq
%fk -> jn, gk
%dv -> zp
%dp -> ph
&mf -> gb, tx, xj, dd, qx, rt, fn
&ph -> nn, xz, tk, ps, qs
%ps -> xz
&km -> gq
broadcaster -> fv, cr, rt, tk
%gk -> jn, xt
%cf -> ph, nz
%tl -> jn, br
%cm -> bj, ph
%nn -> nh
%jp -> mf, dd
%gh -> jn, dj
%hf -> tl, jn
%sl -> jn
%gx -> lv'''

s = '''broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a'''

flows = {}
flip_flops = {}
conj = {}
for line in s.splitlines():
    source, targets = line.split('->')
    targets = str(targets).strip()
    targets = targets.split(',')
    targets = tuple(map(lambda x: x.strip(), targets))
    source = str(source).strip()
    if source.startswith('%'):
        source = source[1:]
        flip_flops[source] = False
    elif source.startswith('&'):
        source = source[1:]
        conj[source] = {}
    flows[source] = targets

for source, targets in flows.items():
    for target in targets:
        if target in conj.keys():
            conj[target].update({source: False})

totals = {False: 0, True: 0}


def sig():
    signals_q = [('button', False, 'broadcaster'), ]
    while len(signals_q):
        source, signal, target = signals_q.pop(0)
        print(source, signal, '->', target)
        totals[signal] += 1
        targets = flows[target]

        new_signal = signal

        if target in flip_flops.keys():
            if not signal:
                flip_flops[target] = not flip_flops[target]
                new_signal = flip_flops[target]
        elif target in conj.keys():
            conj[target][source] = signal
            sigs = conj[target].values()
            all_high = True
            for sig in sigs:
                if not sig:
                    all_high = False
                    break
            new_signal = not all_high

        for t in targets:
            signals_q.append((target, new_signal, t))


sig()

print(totals)  # incomplete
