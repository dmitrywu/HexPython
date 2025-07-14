def diff(ang1, ang2):
    norm_ang1 = (ang1 % 360 + 360) % 360
    norm_ang2 = (ang2 % 360 + 360) % 360
    dumb_diff = abs(norm_ang1 - norm_ang2)
    return min(dumb_diff, 360 - dumb_diff)
