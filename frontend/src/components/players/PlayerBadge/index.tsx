import { Badge, Center, Group } from '@mantine/core'
import { IconUser } from '@tabler/icons-react'
import classes from './PlayerBadge.module.css'

type Props = {
  name: string
}

export default function PlayerBadge({ name }: Props) {
  return (
    <Group gap={8} mb={-8}>
      <Center>
        <IconUser size="1.05rem" className={classes.icon} stroke={1.5} />
        <Badge variant="outline" className="ml-2">
          {name}
        </Badge>
      </Center>
    </Group>
  )
}
