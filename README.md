# DiffTree

### Git Diff between tree-structured file contents.

- The respective colours mean the following operations :-
  > <span style='color: green'>Insertion</span><span>: Text absent in ground truth file, but present in prediction
  file.</span></br>
  <span style='color: red'>Deletion</span><span> : Text present in ground truth file, but absent in prediction
  file.</span>     </br>
  <span style='color:magenta'>Replacement</span><span> : Text from prediction file, to be replaced in ground truth
  file.</span>     
  <span style='color:cyan'>Missing Nodes</span><span> : Indicates tree nodes missing in respective file content.</span>

![output1](imgs/difftree1.png)     

-----
- A sample input file looks like so:    
  > 1 - H - A the response in   
  1.1 - T - And "Interests Consider" to    
  1.1.1 - H - Learning for table encouragement...    
  1.1.1.1 - T - Training pennsylvania take is    
  1.1.1.2 - T - Participants groups Times mentioned    
  1.1.2 - H - Court but young complications    
  1.1.2.1 - T - White elements (light, agreement    
  1.1.2.2 - T - Death central/future provide will    
  1.1.2.3 - T - Purpose can (last america     
  1.1.2.4 - T - Concerning left my amount    
  1.1.2.5 - T - Hand-came york he otherwise     
  1.1.3 - H - Percent may capital congress     
  1.1.3.1 - T - Definition sense maintenance give     
  1.1.3.2 - T - Difficulty instead relation him    
  1.1.4 - H - Outside new south total      
  1.1.4.1 - T - Class-local cultural be persons     
  1.1.4.2 - T - Growth substantial apparently structures     
  1.1.4.3 - T - Energy culture if living     
  1.1.5 - H - Bi our ex see     
  1.1.5.1 - T - Strong expressed thousand ok     
  1.1.5.2 - T - Remember arrangement generation ta      
  1.1.5.3 - T - College essentially civilization friends       
---
