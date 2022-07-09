import intellect

class MyIntellect(Intellect):
        pass

if __name__ == "__main__":
        myIntellect = MyIntellect()

        policy_d = myIntellect.learn(Intellect.local_file_uri("rulesets/test_d.policy"))

        myIntellect.reason(["test_d"])