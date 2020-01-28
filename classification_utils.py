def accuracy(truth_values, predicted_values):
    """
    Computes accuracy (TP+TN)/(TP+TN+FP+FN)
    :param truth_values: true values
    :param predicted_values: predictions

    :return: accuracy
    """
    ### YOUR CODE HERE ###
    y_cv_np=truth_values.to_numpy().reshape(-1)
    y_cv_hat=predicted_values
    tp=0
    tn=0
    fp=0
    fn=0
    for i in range(len(y_cv_np)):
        if y_cv_hat[i]==y_cv_np[i] and y_cv_hat[i]==1:
            tp+=1
        if y_cv_hat[i]==y_cv_np[i] and y_cv_hat[i]==0:
            tn+=1
        if y_cv_hat[i]==1 and y_cv_np[i]==0:
            fp+=1
        if y_cv_hat[i]==0 and y_cv_np[i]==1:
            fn+=1
    accuracy = (tp+tn)/(tp+tn+fp+fn)
    return accuracy
 
    ######################

    return accuracy

def precision(truth_values, predicted_values):
    """
    Computes precision also called positive predicted values(TP/(TP+FP))
    :param truth_values: true values
    :param predicted_values: predictions

    :return: precision
    """
    ### YOUR CODE HERE ###
    y_cv_np=truth_values.to_numpy().reshape(-1)
    y_cv_hat=predicted_values
    tp=0
    tn=0
    fp=0
    fn=0
    for i in range(len(y_cv_np)):
        if y_cv_hat[i]==y_cv_np[i] and y_cv_hat[i]==1:
            tp+=1
        if y_cv_hat[i]==y_cv_np[i] and y_cv_hat[i]==0:
            tn+=1
        if y_cv_hat[i]==1 and y_cv_np[i]==0:
            fp+=1
        if y_cv_hat[i]==0 and y_cv_np[i]==1:
            fn+=1
    precision = tp/(tp+fp)
    return precision

 

 
    ######################

    return precision


def recall(truth_values, predicted_values):
    """
    Computes recall known as sensitivity (TP/TP+FN)
    :param truth_values: true values
    :param predicted_values: predictions

    :return: recall
    """
    ### YOUR CODE HERE ###
    y_cv_np=truth_values.to_numpy().reshape(-1)
    y_cv_hat=predicted_values
    tp=0
    tn=0
    fp=0
    fn=0
    for i in range(len(y_cv_np)):
        if y_cv_hat[i]==y_cv_np[i] and y_cv_hat[i]==1:
            tp+=1
        if y_cv_hat[i]==y_cv_np[i] and y_cv_hat[i]==0:
            tn+=1
        if y_cv_hat[i]==1 and y_cv_np[i]==0:
            fp+=1
        if y_cv_hat[i]==0 and y_cv_np[i]==1:
            fn+=1
    precision = tp/(tp+fn)
    return precision

 

 
    ######################

    return recall

