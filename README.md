---
title: Cisc121FinalProject
emoji: 🐠
colorFrom: yellow
colorTo: pink
sdk: gradio
sdk_version: 6.0.2
app_file: app.py
pinned: false
license: mit
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

Binary Search

I chose this because it is the search that I am most familiar with as well as the search that I use most often. It's logic is very sound and allows for easy visualisation.

Computation Thinking Plan

Decomposition:
- The user provides a sorted list of ints as well as a target int
- create 2 pointers, one at the beginning and one at the end
- calculate the index of the middle element
- compare it to the target
- depending on the comparison adjust left or right pointer
- continue until the element is found or the pointers cross

Pattern Recognition:
- find the middle elment
- identify if the target is in the left half or right half
- elminate the half that cannot house the target

Abstraction:

Info shown:
- list of numbers
- visual indicators for the left, middle and right
- step by step messages explaining what the algorithm is doing

Info hidden:
- the arthimetic behind each pointer movement
- the internal control of flow and loop operations

Algorithmic Design

Input:
- sorted int list
- target value

Output:
- a visual step by step of the algorithm's decisions
- final message that indicates if the target was found and at what index

Time complexity:
- Best Case: O(1) (target is in the middle )
- Average Case: O(log n)
- Worst Case: O(log n)

Space Complexity
-O(1) 



![image](https://cdn-uploads.huggingface.co/production/uploads/69373b71cc6db815a249013b/_yu6B0bEIRmDc6JuRJVqo.png)


![image](https://cdn-uploads.huggingface.co/production/uploads/69373b71cc6db815a249013b/4myHapcm2QEBuO30FznCN.png)


![image](https://cdn-uploads.huggingface.co/production/uploads/69373b71cc6db815a249013b/6JAiK0R73qoCzdv4pi3Ha.png)


![image](https://cdn-uploads.huggingface.co/production/uploads/69373b71cc6db815a249013b/yWCugnWq_EJ9prrKPj75n.png)


![image](https://cdn-uploads.huggingface.co/production/uploads/69373b71cc6db815a249013b/dMyF-W8TZeKCtm9Qh7t9f.png)


![image](https://cdn-uploads.huggingface.co/production/uploads/69373b71cc6db815a249013b/184X0E3Rhk5LJGENkvUou.png)

