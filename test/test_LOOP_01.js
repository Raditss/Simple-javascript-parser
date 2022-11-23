/* Disini uji coba LOOP for */

var A = 4

for (let i = 1; i < 20; i++){
    for (var j = 2; j < 10; j+=1){
        if (A === j){
            break
        }
    }
    if (A === i){
        break
    }
}
