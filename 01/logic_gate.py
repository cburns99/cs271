i = 0
while i < 16:
	print("Mux(a=a[" +str(i)+ "], b=b[" +str(i)+ "], sel=sel[0], out=out1);");
	print("Mux(a=c[" +str(i)+ "], b=d[" +str(i)+ "], sel=sel[0], out=out2);");
	print("Mux(a=out1, b=out2, sel=sel[1], out=out);");
	i += 1