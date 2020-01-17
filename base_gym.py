import gym
import time

env = gym.make('CartPole-v0')  # make your environment!
for i_episode in range(1):
    observation = env.reset()
    for t in range(100):
        time.sleep(0.05)
        env.render()  # render game screen

        # this is random action. replace here to your algorithm!　-> 平均20くらい
        # action = env.action_space.sample()
        
        # 左(0) に進むだけの場合. -> 平均9くらい
        # action = 0

        # ポールの角度と逆に進む場合 -> 平均40くらい
        if observation[2] > 0:
           action = 1   
        else:
           action = 0

        observation, reward, done, info = env.step(
            action)  # get reward and next scene
        if done:
            print("Episode: ", i_episode, " finished after {} timesteps".format(
                t+1), " reward= ", reward)
            break

env.close()
