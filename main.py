
from pyscript import document


def Operation(event):


    num1 = float(document.getElementById("num1").value)
    num2 =float (document.getElementById("num2").value)


    result = num1 + num2 / 2


    document.getElementById("result").innerText = "The Average Of Two digits: " + str(result)