from moviepy.editor import VideoFileClip

input_video = "input.mp4"   
output_gif = "output.gif"   
start_time = 0              
end_time = 5      #you can change the seconds to whatever you want
clip = VideoFileClip(input_video).subclip(start_time, end_time)
clip = clip.resize(width=320)  
clip.write_gif(output_gif)

print(f"✅ GIF saved as: {output_gif}")
