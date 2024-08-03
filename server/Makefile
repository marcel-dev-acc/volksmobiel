# Compiler for C and C++
CC = gcc
CXX = g++

# Compiler flags for C and C++
CFLAGS = -Iinclude
CXXFLAGS = -Iinclude

# Linking flags (none in this simple example)
LDFLAGS = 

# All object files
C_OBJS = src/my_c_module.o
CXX_OBJS = src/main.o

# The executable file
EXEC = my_app

# Rule to build the final executable
all: $(EXEC)

# Rule to link the final executable
$(EXEC): $(C_OBJS) $(CXX_OBJS)
	$(CXX) $(C_OBJS) $(CXX_OBJS) -o $(EXEC) $(LDFLAGS)

# Rule to build C object files
src/%.o: src/%.c
	$(CC) $(CFLAGS) -c $< -o $@

# Rule to build C++ object files
src/%.o: src/%.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Clean up build files
clean:
	rm -f src/*.o $(EXEC)
