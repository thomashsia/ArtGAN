import torch
import torch.nn as nn

x_input = torch.randn(3,3)	#Randomly Generate Inputs
print('x_input:\n', x_input)

y_target = torch.tensor([1,2,0])	# Set the output
print('y_target:\n', y_target)


# Calculate the output using Softmax
softmax_func = nn.Softmax(dim=1)
soft_output = softmax_func(x_input)
print('soft_output:\n', soft_output)

# logarithmize the softmax output
log_output = torch.log(soft_output)
print('log_output:\n', log_output)


# softmax + log == nn.LogSoftmax
logsoftmax_func = nn.LogSoftmax(dim=1)
logsoftmax_output = logsoftmax_func(x_input)
print('logsoftmax_output:\n', logsoftmax_output)


nllloss_func = nn.NLLLoss()
nlloss_output = nllloss_func(logsoftmax_output, y_target)
print('nlloss_output:\n', nlloss_output)


crossentropyloss = nn.CrossEntropyLoss()
crossentropyloss_output = crossentropyloss(x_input, y_target)
print('crossentropyloss_output:\n', crossentropyloss_output)