# Import the game
import gym_super_mario_bros
# Import the Joypad wrapper
from nes_py.wrappers import JoypadSpace
# Import the SIMPLIFIED controls
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT


# Setup game
env = gym_super_mario_bros.make('SuperMarioBros-v0', apply_api_compatibility=True, render_mode="human")
env = JoypadSpace(env, SIMPLE_MOVEMENT)



# Create a flag - restart or not
done = True
# Loop through each frame in the game
for step in range(10000): 
    # Start the game to begin with 
    if done: 
        # Start the game
        env.reset()
    # Do random actions
    # observation, reward, done, info, prob = env.step(1)
    observation, reward, done, info, prob = env.step(env.action_space.sample())
    # state, reward, done, info = env.step(action)
    # Show the game on the screen
    env.render()
# Close the game
env.close()