if (a>b) {
    c = a;
} else {
    c = b;
    if (a>b) {}
    else if (b>c) {
        c = b;
    } else {
        c = c;
    }
}