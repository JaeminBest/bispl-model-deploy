# Vessl-Deploy

## Installation

- vessl install

## Installation Troubleshooting

### pip install vessl 시에 PyYAML 관련 에러가 발생하는 경우

```
pip install vessl --ignore-installed PyYAML
```

### import vessl 시에 "AttributeError: module 'lib' has no attribute 'X509_V_FLAG_CB_ISSUER_CHECK'" 이슈 발생하는 경우

```
pip install pyopenssl --upgrade
```

## Demo (Medical-X-VL)
