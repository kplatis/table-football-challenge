import { useRouter } from 'next/navigation'
import { Button, Card, Group, Text } from '@mantine/core'

type Props = {
  message: string
  buttonMessage: string
  buttonUrl: string
}

export default function MessageWithButton({
  message,
  buttonMessage,
  buttonUrl,
}: Props) {
  const router = useRouter()

  return (
    <Card withBorder p="md" mt="lg">
      <Group gap="md" justify="center">
        <Text>{message}</Text>
        <Button onClick={() => router.push(buttonUrl)}>{buttonMessage}</Button>
      </Group>
    </Card>
  )
}
