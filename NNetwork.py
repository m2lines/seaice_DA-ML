import torch
import torch.nn as nn
from collections import OrderedDict

class CNN(nn.Module):
    """
    Fully CNN with 4 convolutional layers
    The input 'args' should be a dictionary containing
    details of the network hyperparameters and architecture
    """
    
    def __init__(self,args):
        super(CNN, self).__init__()
        torch.manual_seed(args['seed'])

        self.conv_net = nn.Sequential(OrderedDict([
            ('C1', nn.Conv2d(args['n_channels'], args['h_channels'][0], kernel_size=args['kernel_size'],\
                             padding=args['zero_padding'],stride=args['stride'], bias=args['bias'])),
            ('Relu1', nn.ReLU()),
            ('C2', nn.Conv2d(args['h_channels'][0], args['h_channels'][1], kernel_size=args['kernel_size'],\
                             padding=args['zero_padding'],stride=args['stride'],bias=args['bias'])),
            ('Relu2', nn.ReLU()),
            ('C3', nn.Conv2d(args['h_channels'][1], args['h_channels'][2], kernel_size=args['kernel_size'],\
                             padding=args['zero_padding'],stride=args['stride'],bias=args['bias'])),
            ('Relu3', nn.ReLU()),
            ('C4', nn.Conv2d(args['h_channels'][2], args['n_classes'], kernel_size=args['kernel_size'],\
                             padding=args['zero_padding'],stride=args['stride'],bias=args['bias'])),
        ]))

    def forward(self, x):
        return self.conv_net(x)
    
def Net(x_train,y_train,x_valid,y_valid,args,path=None):
    """
    Function to train CNN and/or perform inference.
    Can either provide a 'path' to the pre-computed network weights,
    or leave as None to perform optimization from scratch (the latter
    will be very slow). If path is None, then the optimization will be
    performed using training data 'x_train' and 'y_train'. Inference
    will be done on 'x_valid' and 'y_valid' in either case.
    The input 'args' should be a dictionary containing
    details of the network hyperparameters and architecture
    """
    
    torch.manual_seed(args['seed'])
    
    args['n_channels'] = x_train.shape[1]
    args['n_classes'] = y_train.shape[1]

    train_data = torch.utils.data.TensorDataset(x_train,y_train)
    test_data = torch.utils.data.TensorDataset(x_valid,y_valid)

    model = CNN(args)
    if path is None:
        path = 'CNN_weights.pt'
        opt = torch.optim.Adam(model.parameters(),lr=args['lr'],weight_decay=args['wd'])
        loader_train = torch.utils.data.DataLoader(dataset=train_data, batch_size=args['batch_size'], shuffle=True)
        for epoch in range(args['epochs']):
            for x_,y_ in loader_train:
                opt.zero_grad()
                loss = args['loss'](model(x_),y_)
                loss.backward()
                opt.step()
        torch.save(model.state_dict(),path)
    else:
        model.load_state_dict(torch.load(path,map_location=torch.device('cpu')))
        model.eval()
    f = []
    loader_test = torch.utils.data.DataLoader(dataset=test_data, batch_size=args['batch_size'], shuffle=False)
    with torch.no_grad():
        for xs_,ys_ in loader_test:
            f.append(model(xs_))
    predictions = torch.cat(f).numpy()
    return predictions