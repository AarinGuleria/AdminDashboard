import React, { useMemo } from 'react'
import { User } from '@/graphql/schema.types'
import { Button, Card, ConfigProvider, Dropdown, theme } from 'antd'
import { Text } from '@/components/text'
import { MenuProps } from 'antd/lib'
import { EyeOutlined, MoreOutlined } from '@ant-design/icons'

type ProjectCardProps = {
    id: string,
    title: string,
    updatedAt: string,
    dueDate?: string,
    users?: {
        id: string,
        name: string,
        avatarUrl?: User['avatarUrl']
    }[]
}

const ProjectCard = ({ id, title, dueDate, users }: ProjectCardProps) => {

const { token } = theme.useToken();

const edit =() => {}

const dropdownItems = useMemo(() => {
    const dropdownItems: MenuProps['items'] = [
        {
            label: 'View card',
            key: '1',
            icon: <EyeOutlined />,
            onClick: () => {
                edit()
            }
        },
        {
            danger: true,
            label: 'Delete card',
            key: '2',
            onClick: () => {}
        }
    ]

    return dropdownItems
}, [])

return (
    <ConfigProvider
        theme={{
            components: {
                Tag: {
                    colorText: token.colorTextSecondary,
                },
                Card: {
                    headerBg: 'transparent',
                }
            }
        }}
    >
        <Card
            size="small"
            title={<Text ellipsis={{tooltip: title}}>{title}</Text>}
            onClick={() => edit()}
            extra={
                <Dropdown
                    trigger={["click"]}
                    menu={{
                        items: dropdownItems,
                    }}
            >
                <Button 
                    type= "text"
                    shape= "circle"
                    icon={
                        <MoreOutlined 
                            style={{
                                transform: 'rotate(90deg)'
                            }}
                        />
                    }
                    onPointerDown={(e) => {
                        e.stopPropagation()
                    }}
                />
            </Dropdown>
            }
        >

        </Card>
    </ConfigProvider>
  )
}

export default ProjectCard