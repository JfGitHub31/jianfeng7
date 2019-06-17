function f1() {
    let i=0;

    function f2() {
        i++;
        console.log(i);
    }
    return f2
}

// f1();
// f1()();
// f1()();

f=f1();
f();
f();

