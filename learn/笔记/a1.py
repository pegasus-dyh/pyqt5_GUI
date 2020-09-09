class Baseline(Model):
    def __init__(self):
        super(Baseline, self).__init__()
        self.c1 = Conv2D(filters=6, kernel_size=(5, 5), padding='same')  # 卷积层
        self.b1 = BatchNormalization()  # BN层
        self.a1 = Activation('relu')  # 激活层
        self.p1 = MaxPool2D(pool_size=(2, 2), strides=2, padding='same')  # 池化层
        self.d1 = Dropout(0.2)  # dropout层

        self.flatten = Flatten()
        self.f1 = Dense(128, activation='relu')
        self.d2 = Dropout(0.2)
        self.f2 = Dense(10, activation='softmax')

    def call(self, x):
        x = self.c1(x)
        x = self.b1(x)
        x = self.a1(x)
        x = self.p1(x)
        x = self.d1(x)

        x = self.flatten(x)
        x = self.f1(x)
        x = self.d2(x)
        y = self.f2(x)
        return y




Model=Sequential([
    Conv2D(fliters=6,kernel_size=(5, 5), padding='same',activation='relu'),
    BatchNormalization(),
    MaxPool2D(pool_size=(2, 2), strides=2, padding='same'),
    Dropout(0.2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.2),
    Dense(10, activation='softmax')
])


inputs = tf.keras.Input(shape=(维度))
conv1=Conv2D(fliters=6,kernel_size=(5, 5), padding='same',activation='relu')(inouts)
bn=BatchNormalization()(conv1)
maxp=MaxPool2D(pool_size=(2, 2), strides=2, padding='same')(bn)
dout1=Dropout(0.2)(maxp)
faltten=Flatten()(dout)
d1=Dense(128, activation='relu')(flatten)
dout2=Dropout(0.2)(d1)
outputs=Dense(10, activation='softmax')(dout2)
model=tf.keras.Model(inputs=inputs, outputs=outputs)
