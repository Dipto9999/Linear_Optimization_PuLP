## Linear Programming Problem 1.0
```math
    \begin{align*}
        {\rm Minimize} \hspace{5mm}
            x_1 - 3x_2 - x_3 \\
        {\rm Subject \hspace{1mm} to} \hspace{5mm}
            x_1 + x_2 + x_3 = 3 \\
            -x_1 + x_2 	\leq 1 \\
            x_1 \geq 0 \\
            x_2 {\hspace{1mm} unconstrained} \\
            x_3 \geq 0 \\
    \end{align*}

    ### Standard Inequality Form

    \begin{align*}
        {\rm Maximize} \hspace{5mm}
            -x_1 + 3x_2^{+} - 3x_2^{-} + x_3 \\
        {\rm Subject \hspace{1mm} to} \hspace{5mm}
            x_1 + x_2^{+} - x_2^{-} + x_3 \leq 3 \\
            -x_1 - x_2^{+} + x_2^{-} - x_3 \leq -3 \\
            -x_1 + x_2^{+} - x_2^{-} \leq 1 \\
            x_1, x_2^{+}, x_2^{-}, x_3 \geq 0 \\
    \end{align*}
```