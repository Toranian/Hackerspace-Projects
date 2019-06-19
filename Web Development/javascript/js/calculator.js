function calc() {
  var num1 = parseInt(document.querySelector("#value1").value);
  var num2 = parseInt(document.querySelector("#value2").value);
  var op = document.querySelector("#operator").value;
  var calculate;

  if (op == "add") {
    calculate = num1 + num2;
  }
  if (op == "min") {
    calculate = num1 - num2;
  }
  if (op == "div") {
    calculate = num1 / num2;
  }
  if (op == "mult") {
    calculate = num1 * num2;
  }


  console.log(calculate);

  document.querySelector("#result").innerHTML = calculate;

}
