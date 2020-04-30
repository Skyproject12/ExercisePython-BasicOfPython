data_int = 1 
print("data =", data_int, "type", type(data_int)) 

# casting data into type float 
# float akan automatis dibulatkan ke bawah
# string harus angka untuk diterjemahkan ke dalam int  
# untuk membuat data string false ketika di convert ke boolean maka harus membuat data string kosong ""
data_float = float(data_int) 
data_str = str(data_int) 
data_bool = bool(data_int) 
print("data =", data_float, "type", type(data_float))
print("data =", data_str, "type", type(data_str))
print("data =", data_bool, "type", type(data_bool))