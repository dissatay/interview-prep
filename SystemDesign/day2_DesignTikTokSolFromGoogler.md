#Google Soft. Engineer designs Tik Tok 
https://www.youtube.com/watch?v=Z-0g_aJL5Fw&t=7s

 ## Functional Requirments:
 1. upload videos + text.  Create API that is client agnostic.
 2. video feed of people we follow.
 3. video interaction.  follow users, commenting, liking.
 
 ## Non-Functional Requirements: ()
 1. Availability. Needs to be a highly available system.  Around 99.999%
 2. Latency.  TBD. maybe Cache stuff on the device quickly.
 3. Scale.  He asks for a rough estimate of users in a day. interviewer says a million daily active users.
 
 ## Estimates 
- assumption 1 min. of compressed h.264 video is about 5 MB 
- User uploads 2 videos per day per user 
- User metadata 1k per user per day 

Total_Mem_Day_per_User = (5MB video ) * 2 videos / user


## Objects 
o1 
userid    | uuid
vido_link : url
meta      : string 

o2 
userid     | uuid
following  : foreign key to database x
likes      : foreign key to database y


## DataBase 
- relational database. 
- database 1 holds links to videos 
- database 2 holds the actual video 
- database 3 read only database 

## Requests
- Get request.  

## Cache   (system seems very load heavy)
-  grab the top videos that are preselected.
- pre-cache service
- runs on a schedule or on demand 
- compiles a playlist and pre-caches them
- base it on when the user goes and fetches one, it preloads next

## Bottlenecks 
- regions.  if multiple regions, geo-locate users
- load balancer in front of API endpoints.
- database sharding. 