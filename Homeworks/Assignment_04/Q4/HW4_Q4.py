import math

def sigmoid(x):
    return round(1.0/(1 + math.exp(-x)), 8)

input1 = [0, 0, 1]
input2 = [0, 1, 1]
input3 = [1, 0, 1]
input4 = [1, 1, 1]

W_nuron1 = [0.57355803, 1.14075424, -0.74729319]
W_nuron2 = [4.33381305, 4.13435859, -0.4652327]
W_nuron3 = [4.48264021, -6.72940986, -1.69616486]
W_nuron4 = [7.17923159, -5.48075242, 2.27117356]

Sec_layer = [-1.00453775, 5.89444927, 10.35035355, -10.16747511]

def NN(arr):
    
    # Hidden layer
    nur1 = sigmoid((arr[0] * W_nuron1[0] + arr[1] * W_nuron1[1] + arr[2] * W_nuron1[2]) + 0 )
    nur2 = sigmoid((arr[0] * W_nuron2[0] + arr[1] * W_nuron2[1] + arr[2] * W_nuron2[2]) + 0 )
    nur3 = sigmoid((arr[0] * W_nuron3[0] + arr[1] * W_nuron3[1] + arr[2] * W_nuron3[2]) + 0 )
    nur4 = sigmoid((arr[0] * W_nuron4[0] + arr[1] * W_nuron4[1] + arr[2] * W_nuron4[2]) + 0 )

    # Output layer
    outPut1 = nur1 * Sec_layer[0]
    outPut2 = nur2 * Sec_layer[1]
    outPut3 = nur3 * Sec_layer[2]
    outPut4 = nur4 * Sec_layer[3] 

    print("\nThis is the final answer: ")
    print(sigmoid(outPut1 + outPut2 + outPut3 + outPut4))

NN(input1)
NN(input2)
NN(input3)
NN(input4)

