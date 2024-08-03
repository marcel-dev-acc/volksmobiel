#include <iostream>
extern "C" {
    #include "my_c_module.h"
}

int main() {
    std::cout << "Calling C function from C++..." << std::endl;
    c_function();
    return 0;
}