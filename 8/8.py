class Student:
    name= "Викторович"
    surname= "Солнечный"
    def show(self):
        return self.cape(self.name)
    def cape(self,stri):
        return stri.upper()
st=Student    
st.show()
