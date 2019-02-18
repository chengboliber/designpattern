# -*- coding:utf-8 -*-


def decorator_singleton(cls):
    """
    装饰器实现方式
    :param cls:
    :return:
    """
    instances = {}

    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)

    return _singleton


class NewSingleton(object):
    """
    需要单例实现的类继承该类
    注意：该方法不适用于多线程下的单例模式
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(NewSingleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class DstClass(object):
    """
    模块实例引用法, 直接实例化目标类，其他地方引用该类时，就是永远都是单例模式
    """
    def __init__(self, *args, **kwargs):
        pass


DstClass = DstClass()
