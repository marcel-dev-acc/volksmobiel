CXX       := g++
CXX_FLAGS := -Wall -Wextra -std=c++17 -ggdb

BIN     := bin
SRC     := src
INCLUDE := include
LIB     := lib
LIBRARIES   := 
EXECUTABLE  := main

build:
	@echo "🚧 Building..."
	$(CXX) $(SRC)/*.cpp -o $(BIN)/$(EXECUTABLE)

run:
	@clear
	@echo "🚀 Executing..."
	$(BIN)/$(EXECUTABLE)

clean:
	@echo "🧹 Clearing..."
	-rm $(BIN)/*
