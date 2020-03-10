# videoclip
## Command Format
NAME
       videoclip - Cut video file

SYNOPSIS:

  videoclip [videoname]
  
DESCRIPTION  

  Usage: videoclip [videoname]
  After run command it will asked for the start time, end time and cut type of operation. 
  
  start time
  
    Cut from this time. Parameter format: HH:MM:SS or HH:MM:SS.S

  end time
  
    Cut end to this time. Parameter format: HH:MM:SS or HH:MM:SS.S
    
  cut type
  
    fast
      Cut care about key frame. It will get the last key frame before [start time]
    fastwithoutcarekeyframe
      Cut start from [Start time]. Sometime, it will make video and audio async
    exact:
      Start exact from [start time] without care about key frame. video will be redecoded by video codec: libx264 and audio codec: aac 

AUTHOR

       Written by Huang, Baogui.
       Email: bghuang@foxmail.com
