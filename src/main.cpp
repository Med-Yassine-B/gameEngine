#include <SDL2/SDL.h>
#include <windows.h>
#include <iostream>
#define FULL 255

void draw();
void update();
void start();

int fps=30;
int width=480,height=480;
SDL_Window* window;
SDL_Renderer* renderer;
SDL_Event event;
SDL_Keycode key;





//------start function------- 
void start(){
    if (SDL_Init(SDL_INIT_VIDEO) != 0) {
        SDL_Log("Failed to initialize SDL: %s", SDL_GetError());
    }
    window = SDL_CreateWindow("Yellow Square", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, width, height, 0);
    if (window == NULL) {
        SDL_Log("Failed to create window: %s", SDL_GetError());
        SDL_Quit();
    }
    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    if (renderer == NULL) {
        SDL_Log("Failed to create renderer: %s", SDL_GetError());
        SDL_DestroyWindow(window);
        SDL_Quit();
    }

}

//_______update the game______
void update(){

    Sleep(1000/fps);
}

//---------rendering the game---
void draw(){

}
//----UI rendering-------


int main(int argc, char* argv[]) {
    start();
    bool quit = false;
    while (!quit) {
      //---events- _ADD_QUIT_BUtton #DONE_ 
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                std::cout<<"Quit";
                quit = true;
            }
            if(event.type==SDL_KEYUP){
                if(key==event.key.keysym.sym)
                    key=0;
            }
            if(event.type==SDL_KEYDOWN){
                key=event.key.keysym.sym;
                if(event.key.keysym.sym==27)
                  quit=true;
            }
        
        }
        update();
    }
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 1;
}
