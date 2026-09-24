import numpy as np

# Suppose we want the first k slices of the dimension at index 'i'
# regardless of how many dimensions come before it.
def get_subslice(arr, axis_index, k):
    if k > 0:
        # This dynamically builds a slice tuple
        slc = [slice(None)] * arr.ndim
        slc[axis_index] = list(range(k))
        return arr[tuple(slc)]
    else:
        return np.empty_like(arr)
        

def add_past_windows(\
        A : np.ndarray,\
        lb : int,\
        strict_lookback : bool,\
        axis : int = 0,\
    ) -> np.ndarray:

    """
        A : a n-dimensional tensor.
        lb : the rolling windows size.
        strict_lookback = True -> exclude the value at timestamp T from the rolling window constructed for time T.
        axis : the axis along which to compute the rolling window.


        returns:
            A_dimsxW : a (n+1)-dimensional tensor with the last dimension being the window's dimension
    """

    ## the length of M along the axis 'axis' will be reduced by 'lb-1'.
    
    M = np.lib.stride_tricks.sliding_window_view(x=A, window_shape=lb+(1 if strict_lookback else 0), axis=axis)
    if strict_lookback is True:
        M = M[..., :-1] ## drop the most recent element since we have 'strict_lookback'='True'
    
    if A.shape[axis]-M.shape[axis] > 0:
        M_padding = np.zeros(M.shape)
        M_padding = get_subslice(M_padding, axis_index=axis, k=A.shape[axis]-M.shape[axis])
        M = np.concatenate(( M_padding, M), axis=axis)
    return M 


def add_future_windows(\
        A : np.ndarray,\
        lb : int,\
        strict_lookahead : bool,\
        axis : int = 0,\
    ) -> np.ndarray:

    """
        A : a n-dimensional tensor.
        lb : the rolling windows size.
        strict_lookahead = True -> exclude the value at timestamp T from the rolling window constructed for time T.
        axis : the axis along which to compute the rolling window.


        returns:
            A_dimsxW : a (n+1)-dimensional tensor with the last dimension being the window's dimension
    """

    ## the length of M along the axis 'axis' will be reduced by 'lb-1'.
    reversedA = np.flip(A, axis=axis)
    M = np.lib.stride_tricks.sliding_window_view(x=reversedA, window_shape=lb+(1 if strict_lookahead else 0), axis=axis)
    M = np.flip(M, axis=axis)
    M = np.flip(M, axis=-1)
    if strict_lookahead is True:
        M = M[..., 1:] ## drop the most recent element since we have 'strict_lookahead'='True'

    if A.shape[axis]-M.shape[axis] > 0:
        M_padding = np.zeros(M.shape)
        M_padding = get_subslice(M_padding, axis_index=axis, k=A.shape[axis]-M.shape[axis])
        M = np.concatenate(( M, M_padding), axis=axis)
    return M

