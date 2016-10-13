function writeFib(){
	const readline = require('readline');
	const prompts = readline.createInterface(process.stdin, process.stdout);
	var num = prompts.question("Pick a number less than 100 and greater than 0: ", function(inp){
		//asked for the input

		if(inp > 0 && inp < 101){	//checked for the input
			var fiboHolder = [];// the actual printed sequence

						function fibo(a){
								if(a<2){
										return a;
								}
								else{
										return fibo(a-1)+fibo(a-2);
								}
						}

						for(i=1; i<=inp; i++){
								fiboHolder.push(fibo(i));
						}

			}

			console.log("Fibonacci Sequence with "+inp+" characters is "+fiboHolder);// user gets the output

			prompts.close();
		}else{// if inp is not less than 0 and greater than 100
			console.log('You have to pick a number less than 100 and greater than 0: ');
			writeE();//function runs again
		}
		});// closing var num

}// closing writeFib()

writeFib();
